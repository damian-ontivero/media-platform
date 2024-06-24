import { Movie, MovieParams } from "@/contexts/backoffice/movies/domain/Movie";
import { MovieRepository } from "@/contexts/backoffice/movies/domain/MovieRepository";
import { PaginatedResponse } from "@/contexts/shared/domain/PaginatedResponse";

const API_URL = "http://localhost:8000/api/v0/movies";

export class HTTPMovieRepository implements MovieRepository {
    async matching(): Promise<PaginatedResponse<Movie>> {
        const response = await fetch(API_URL);
        const paginatedResponse = await response.json();
        return {
            pageSize: paginatedResponse.pageSize,
            pageNumber: paginatedResponse.pageNumber,
            totalPages: paginatedResponse.totalPages,
            items: paginatedResponse.items.map(
                (movie: MovieParams) => new Movie({ id: movie.id, title: movie.title, mediaId: movie.mediaId })
            ),
        };
    }

    async search(id: string): Promise<Movie | null> {
        const response = await fetch(`${API_URL}/${id}`);
        const movie = await response.json();
        return new Movie({ id: movie.id, title: movie.title, mediaId: movie.mediaId });
    }

    async create(movie: Movie): Promise<void> {
        await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(movie),
        });
    }

    async update(movie: Movie): Promise<void> {
        await fetch(`${API_URL}/${movie.getId()}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(movie),
        });
    }

    async delete(id: string): Promise<void> {
        await fetch(`${API_URL}/${id}`, {
            method: "DELETE",
        });
    }
}
