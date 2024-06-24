import { MediaFinder } from "@/contexts/backoffice/media/application/MediaFinder";
import { HTTPMediaRepository } from "@/contexts/backoffice/media/infrastructure/persistence/http/HTTPMediaRepository";

export async function useMedia(id: string) {
    const mediaRepository = new HTTPMediaRepository();
    const mediaFinder = new MediaFinder(mediaRepository);

    return await mediaFinder.run(id);
}
