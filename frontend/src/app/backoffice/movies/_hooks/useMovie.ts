import { MovieFinder } from "@/contexts/backoffice/movies/application/MovieFinder";
import { Movie } from "@/contexts/backoffice/movies/domain/Movie";
import { HTTPMovieRepository } from "@/contexts/backoffice/movies/infrastructure/persistence/http/HTTPMovieRepository";
import { useEffect, useState } from "react";

export function useMovie(id: string) {
    const [data, setData] = useState<Movie | null>(null);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState<Error | null>(null);

    useEffect(() => {
        const movieRepository = new HTTPMovieRepository();
        const movieFinder = new MovieFinder(movieRepository);
        let isCancelled = false;

        const fetchData = async () => {
            try {
                const response = await movieFinder.run(id);
                if (!isCancelled) {
                    setData(response);
                }
            } catch (error) {
                if (!isCancelled) {
                    setError(error as Error);
                }
            } finally {
                if (!isCancelled) {
                    setIsLoading(false);
                }
            }
        };

        fetchData();

        return () => {
            isCancelled = true;
        };
    }, []); // Empty array means this effect will run once

    return {
        data,
        isLoading,
        error,
    };
}
