import { SerieEpisode } from "./SerieEpisode";

export type SerieSeasonParams = {
    id: string;
    number: number;
    episodes: SerieEpisode[];
};

export class SerieSeason {
    private readonly id: string;
    private readonly number: number;
    private readonly episodes: SerieEpisode[];

    constructor(id: string, number: number, episodes: SerieEpisode[]) {
        this.id = id;
        this.number = number;
        this.episodes = episodes;
    }

    getId(): string {
        return this.id;
    }

    getNumber(): number {
        return this.number;
    }

    getEpisodes(): SerieEpisode[] {
        return this.episodes;
    }
}
