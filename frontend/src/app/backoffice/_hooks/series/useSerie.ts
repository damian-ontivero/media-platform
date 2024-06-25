import { SerieFinder } from "@/contexts/backoffice/series/application/SerieFinder";
import { Serie } from "@/contexts/backoffice/series/domain/Serie";
import { HTTPSerieRepository } from "@/contexts/backoffice/series/infrastructure/persistence/http/HTTPSerieRepository";
import { useEffect, useState } from "react";

export function useSerie(id: string) {
    const [data, setData] = useState<Serie | null>(null);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState<Error | null>(null);

    useEffect(() => {
        const serieRepository = new HTTPSerieRepository();
        const serieFinder = new SerieFinder(serieRepository);
        let isCancelled = false;

        const fetchData = async () => {
            try {
                const response = await serieFinder.run(id);
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
