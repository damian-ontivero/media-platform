import { Media } from "./Media";

export type PaginatedResponse<T> = {
    pageSize: number;
    pageNumber: number;
    totalPages: number;
    items: T[];
};

export interface MediaRepository {
    matching(): Promise<PaginatedResponse<Media>>;
    search(id: string): Promise<Media | null>;
    create(media: Media): Promise<void>;
    update(media: Media): Promise<void>;
    delete(id: string): Promise<void>;
}
