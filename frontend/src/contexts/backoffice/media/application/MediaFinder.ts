import { Media } from "@/contexts/backoffice/media/domain/Media";
import { MediaRepository } from "@/contexts/backoffice/media/domain/MediaRepository";

export class MediaFinder {
    private readonly mediaRepository: MediaRepository;

    constructor(mediaRepository: MediaRepository) {
        this.mediaRepository = mediaRepository;
    }

    async run(id: string): Promise<Media | null> {
        return await this.mediaRepository.search(id);
    }
}
