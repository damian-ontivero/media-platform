import { Serie } from "@/contexts/backoffice/series/domain/Serie";
import { PaginatedResponse, SerieRepository } from "@/contexts/backoffice/series/domain/SerieRepository";

export class SerieSearcher {
    private readonly serieRepository: SerieRepository;

    constructor(serieRepository: SerieRepository) {
        this.serieRepository = serieRepository;
    }

    async run(): Promise<PaginatedResponse<Serie>> {
        return await this.serieRepository.matching();
    }
}
