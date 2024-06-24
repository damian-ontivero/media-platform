import { Movie } from "@/contexts/backoffice/movies/domain/Movie";
import { MovieRepository } from "@/contexts/backoffice/movies/domain/MovieRepository";

export class MovieFinder {
    private readonly movieRepository: MovieRepository;

    constructor(movieRepository: MovieRepository) {
        this.movieRepository = movieRepository;
    }

    async run(id: string): Promise<Movie | null> {
        return await this.movieRepository.search(id);
    }
}
