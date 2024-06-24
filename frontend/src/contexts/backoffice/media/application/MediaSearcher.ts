import { Media } from "@/contexts/backoffice/media/domain/Media";
import { MediaRepository } from "@/contexts/backoffice/media/domain/MediaRepository";
import { PaginatedResponse } from "@/contexts/shared/domain/PaginatedResponse";

export class MediaSearcher {
    private readonly mediaRepository: MediaRepository;

    constructor(mediaRepository: MediaRepository) {
        this.mediaRepository = mediaRepository;
    }

    async run(): Promise<PaginatedResponse<Media>> {
        return await this.mediaRepository.matching();
    }
}
