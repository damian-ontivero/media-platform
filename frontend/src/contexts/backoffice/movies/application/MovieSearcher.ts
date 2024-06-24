import { Movie } from "@/contexts/backoffice/movies/domain/Movie";
import { MovieRepository } from "@/contexts/backoffice/movies/domain/MovieRepository";
import { PaginatedResponse } from "@/contexts/shared/domain/PaginatedResponse";

export class MovieSearcher {
    private readonly movieRepository: MovieRepository;

    constructor(movieRepository: MovieRepository) {
        this.movieRepository = movieRepository;
    }

    async run(): Promise<PaginatedResponse<Movie>> {
        return await this.movieRepository.matching();
    }
}
