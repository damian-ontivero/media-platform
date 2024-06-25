import { MediaSearcher } from "@/contexts/backoffice/media/application/MediaSearcher";
import { Media } from "@/contexts/backoffice/media/domain/Media";
import { HTTPMediaRepository } from "@/contexts/backoffice/media/infrastructure/persistence/http/HTTPMediaRepository";
import { PaginatedResponse } from "@/contexts/shared/domain/PaginatedResponse";
import { useEffect, useState } from "react";

export function useMedias() {
    const [data, setData] = useState<PaginatedResponse<Media> | null>(null);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState<Error | null>(null);

    useEffect(() => {
        const mediaRepository = new HTTPMediaRepository();
        const mediaSearcher = new MediaSearcher(mediaRepository);
        let isCancelled = false;

        const fetchData = async () => {
            try {
                const response = await mediaSearcher.run();
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
    }, []);

    return {
        data,
        isLoading,
        error,
    };
}
