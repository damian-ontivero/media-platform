import { Serie } from "@/contexts/backoffice/series/domain/Serie";
import { SerieRepository } from "@/contexts/backoffice/series/domain/SerieRepository";
import { PaginatedResponse } from "@/contexts/shared/domain/PaginatedResponse";

export class SerieSearcher {
    private readonly serieRepository: SerieRepository;

    constructor(serieRepository: SerieRepository) {
        this.serieRepository = serieRepository;
    }

    async run(): Promise<PaginatedResponse<Serie>> {
        return await this.serieRepository.matching();
    }
}
