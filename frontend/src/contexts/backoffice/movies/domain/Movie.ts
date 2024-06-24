export type MovieParams = {
    id: string;
    title: string;
    mediaId: string;
};

export class Movie {
    private readonly id: string;
    private readonly title: string;
    private readonly mediaId: string;

    constructor(id: string, title: string, mediaId: string) {
        this.id = id;
        this.title = title;
        this.mediaId = mediaId;
    }

    getId(): string {
        return this.id;
    }

    getTitle(): string {
        return this.title;
    }

    getMediaId(): string {
        return this.mediaId;
    }
}
