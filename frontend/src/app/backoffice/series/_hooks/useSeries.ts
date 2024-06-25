import { SerieSearcher } from "@/contexts/backoffice/series/application/SerieSearcher";
import { Serie } from "@/contexts/backoffice/series/domain/Serie";
import { HTTPSerieRepository } from "@/contexts/backoffice/series/infrastructure/persistence/http/HTTPSerieRepository";
import { PaginatedResponse } from "@/contexts/shared/domain/PaginatedResponse";
import { useEffect, useState } from "react";

export function useSeries() {
    const [data, setData] = useState<PaginatedResponse<Serie> | null>(null);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState<Error | null>(null);

    useEffect(() => {
        const serieRepository = new HTTPSerieRepository();
        const serieSearcher = new SerieSearcher(serieRepository);
        let isCancelled = false;

        const fetchData = async () => {
            try {
                const response = await serieSearcher.run();
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
