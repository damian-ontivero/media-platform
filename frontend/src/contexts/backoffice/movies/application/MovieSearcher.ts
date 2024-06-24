import { Movie } from "@/contexts/backoffice/movies/domain/Movie";
import { MovieRepository, PaginatedResponse } from "@/contexts/backoffice/movies/domain/MovieRepository";

export class MovieSearcher {
    private readonly movieRepository: MovieRepository;

    constructor(movieRepository: MovieRepository) {
        this.movieRepository = movieRepository;
    }

    async run(): Promise<PaginatedResponse<Movie>> {
        return await this.movieRepository.matching();
    }
}
