import { Serie } from "@/contexts/backoffice/series/domain/Serie";
import { SerieRepository } from "@/contexts/backoffice/series/domain/SerieRepository";

export class SerieFinder {
    private readonly serieRepository: SerieRepository;

    constructor(serieRepository: SerieRepository) {
        this.serieRepository = serieRepository;
    }

    async run(id: string): Promise<Serie | null> {
        return await this.serieRepository.search(id);
    }
}
