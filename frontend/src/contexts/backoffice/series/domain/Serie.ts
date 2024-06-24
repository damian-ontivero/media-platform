import { SerieSeason } from "./SerieSeason";

export type SerieParams = {
    id: string;
    title: string;
    seasons: SerieSeason[];
};

export class Serie {
    private readonly id: string;
    private readonly title: string;
    private readonly seasons: SerieSeason[];

    constructor({ id, title, seasons }: SerieParams) {
        this.id = id;
        this.title = title;
        this.seasons = seasons;
    }

    getId(): string {
        return this.id;
    }

    getTitle(): string {
        return this.title;
    }

    getSeasons(): SerieSeason[] {
        return this.seasons;
    }
}
