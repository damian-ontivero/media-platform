import { PaginatedResponse } from "@/contexts/shared/domain/PaginatedResponse";
import { Media } from "./Media";

export interface MediaRepository {
    matching(): Promise<PaginatedResponse<Media>>;
    search(id: string): Promise<Media | null>;
    create(media: Media): Promise<void>;
    update(media: Media): Promise<void>;
    delete(id: string): Promise<void>;
}
