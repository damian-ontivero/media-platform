import { Media, MediaParams } from "@/contexts/backoffice/media/domain/Media";
import { MediaRepository, PaginatedResponse } from "@/contexts/backoffice/media/domain/MediaRepository";

const API_URL = "http://localhost:8000/api/v0/media";

export class HTTPMediaRepository implements MediaRepository {
    async matching(): Promise<PaginatedResponse<Media>> {
        const response = await fetch(API_URL);
        const paginatedResponse = await response.json();
        return {
            pageSize: paginatedResponse.pageSize,
            pageNumber: paginatedResponse.pageNumber,
            totalPages: paginatedResponse.totalPages,
            items: paginatedResponse.items.map(
                (media: MediaParams) => new Media(media.id, media.title, media.size, media.duration, media.path)
            ),
        };
    }

    async search(id: string): Promise<Media | null> {
        const response = await fetch(`${API_URL}/${id}`);
        const media = await response.json();
        return new Media(media.id, media.title, media.size, media.duration, media.path);
    }

    async create(media: Media): Promise<void> {
        await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(media),
        });
    }

    async update(media: Media): Promise<void> {
        await fetch(`${API_URL}/${media.getId()}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(media),
        });
    }

    async delete(id: string): Promise<void> {
        await fetch(`${API_URL}/${id}`, {
            method: "DELETE",
        });
    }
}
