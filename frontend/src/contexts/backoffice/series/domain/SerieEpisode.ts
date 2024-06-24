export type SerieEpisodeParams = {
    id: string;
    number: number;
    title: string;
    mediaId: string;
};

export class SerieEpisode {
    private readonly id: string;
    private readonly number: number;
    private readonly title: string;
    private readonly mediaId: string;

    constructor({ id, number, title, mediaId }: SerieEpisodeParams) {
        this.id = id;
        this.number = number;
        this.title = title;
        this.mediaId = mediaId;
    }

    getId(): string {
        return this.id;
    }

    getNumber(): number {
        return this.number;
    }

    getTitle(): string {
        return this.title;
    }

    getMediaId(): string {
        return this.mediaId;
    }
}
