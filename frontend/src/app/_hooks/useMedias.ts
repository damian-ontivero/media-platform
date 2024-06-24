import { MediaSearcher } from "@/contexts/backoffice/media/application/MediaSearcher";
import { HTTPMediaRepository } from "@/contexts/backoffice/media/infrastructure/persistence/http/HTTPMediaRepository";

export async function useMedias() {
    const mediaRepository = new HTTPMediaRepository();
    const mediaSearcher = new MediaSearcher(mediaRepository);

    return await mediaSearcher.run();
}
