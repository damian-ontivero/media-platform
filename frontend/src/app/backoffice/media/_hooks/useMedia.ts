import { MediaFinder } from "@/contexts/backoffice/media/application/MediaFinder";
import { Media } from "@/contexts/backoffice/media/domain/Media";
import { HTTPMediaRepository } from "@/contexts/backoffice/media/infrastructure/persistence/http/HTTPMediaRepository";
import { useEffect, useState } from "react";

export function useMedia(id: string) {
    const [data, setData] = useState<Media | null>(null);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState<Error | null>(null);

    useEffect(() => {
        const mediaRepository = new HTTPMediaRepository();
        const mediaFinder = new MediaFinder(mediaRepository);
        let isCancelled = false;

        const fetchData = async () => {
            try {
                const response = await mediaFinder.run(id);
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
