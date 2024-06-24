import { Media } from "@/contexts/backoffice/media/domain/Media";
import { MediaRepository, PaginatedResponse } from "@/contexts/backoffice/media/domain/MediaRepository";

export class MediaSearcher {
    private readonly mediaRepository: MediaRepository;

    constructor(mediaRepository: MediaRepository) {
        this.mediaRepository = mediaRepository;
    }

    async run(): Promise<PaginatedResponse<Media>> {
        return await this.mediaRepository.matching();
    }
}
