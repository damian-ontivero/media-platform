import { MovieFinder } from "@/contexts/backoffice/movies/application/MovieFinder";
import { HTTPMovieRepository } from "@/contexts/backoffice/movies/infrastructure/persistence/http/HTTPMovieRepository";

export async function useMovie(id: string) {
    const movieRepository = new HTTPMovieRepository();
    const movieFinder = new MovieFinder(movieRepository);

    return await movieFinder.run(id);
}
