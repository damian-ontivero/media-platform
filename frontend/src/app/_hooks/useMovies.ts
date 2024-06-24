import { MovieSearcher } from "@/contexts/backoffice/movies/application/MovieSearcher";
import { HTTPMovieRepository } from "@/contexts/backoffice/movies/infrastructure/persistence/http/HTTPMovieRepository";

export async function useMovies() {
    const movieRepository = new HTTPMovieRepository();
    const movieSearcher = new MovieSearcher(movieRepository);

    return await movieSearcher.run();
}
