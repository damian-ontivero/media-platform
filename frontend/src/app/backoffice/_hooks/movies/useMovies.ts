import { MovieSearcher } from "@/contexts/backoffice/movies/application/MovieSearcher";
import { Movie } from "@/contexts/backoffice/movies/domain/Movie";
import { HTTPMovieRepository } from "@/contexts/backoffice/movies/infrastructure/persistence/http/HTTPMovieRepository";
import { PaginatedResponse } from "@/contexts/shared/domain/PaginatedResponse";
import { useEffect, useState } from "react";

export function useMovies() {
    const [data, setData] = useState<PaginatedResponse<Movie> | null>(null);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState<Error | null>(null);

    useEffect(() => {
        const movieRepository = new HTTPMovieRepository();
        const movieSearcher = new MovieSearcher(movieRepository);
        let isCancelled = false;

        const fetchData = async () => {
            try {
                const response = await movieSearcher.run();
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
