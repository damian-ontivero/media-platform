import { Serie, SerieParams } from "@/contexts/backoffice/series/domain/Serie";
import { PaginatedResponse, SerieRepository } from "@/contexts/backoffice/series/domain/SerieRepository";

const API_URL = "http://localhost:8000/api/v0/series";

export class HTTPSerieRepository implements SerieRepository {
    async matching(): Promise<PaginatedResponse<Serie>> {
        const response = await fetch(API_URL);
        const paginatedResponse = await response.json();
        return {
            pageSize: paginatedResponse.pageSize,
            pageNumber: paginatedResponse.pageNumber,
            totalPages: paginatedResponse.totalPages,
            items: paginatedResponse.items.map((serie: SerieParams) => new Serie(serie.id, serie.title, serie.seasons)),
        };
    }

    async search(id: string): Promise<Serie | null> {
        const response = await fetch(`${API_URL}/${id}`);
        const serie = await response.json();
        return new Serie(serie.id, serie.title, serie.seasons);
    }

    async create(serie: Serie): Promise<void> {
        await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(serie),
        });
    }

    async update(serie: Serie): Promise<void> {
        await fetch(`${API_URL}/${serie.getId()}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(serie),
        });
    }

    async delete(id: string): Promise<void> {
        await fetch(`${API_URL}/${id}`, {
            method: "DELETE",
        });
    }
}
