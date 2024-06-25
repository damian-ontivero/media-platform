import { Media, MediaParams } from "@/contexts/backoffice/media/domain/Media";
import { MediaRepository } from "@/contexts/backoffice/media/domain/MediaRepository";
import { PaginatedResponse } from "@/contexts/shared/domain/PaginatedResponse";

const API_URL = "http://localhost:8000/backoffice/api/v0/media";

export class HTTPMediaRepository implements MediaRepository {
    async matching(): Promise<PaginatedResponse<Media>> {
        const response = await fetch(API_URL);
        const paginatedResponse = await response.json();
        return {
            pageSize: paginatedResponse.pageSize,
            pageNumber: paginatedResponse.pageNumber,
            totalPages: paginatedResponse.totalPages,
            items: paginatedResponse.items.map(
                (media: MediaParams) =>
                    new Media({
                        id: media.id,
                        title: media.title,
                        size: media.size,
                        duration: media.duration,
                        path: media.path,
                    })
            ),
        };
    }

    async search(id: string): Promise<Media | null> {
        const response = await fetch(`${API_URL}/${id}`);
        const media = await response.json();
        return new Media({
            id: media.id,
            title: media.title,
            size: media.size,
            duration: media.duration,
            path: media.path,
        });
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
