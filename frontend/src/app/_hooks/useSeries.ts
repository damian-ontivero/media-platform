import { SerieSearcher } from "@/contexts/backoffice/series/application/SerieSearcher";
import { HTTPSerieRepository } from "@/contexts/backoffice/series/infrastructure/persistence/http/HTTPSerieRepository";

export async function useSeries() {
    const serieRepository = new HTTPSerieRepository();
    const serieSearcher = new SerieSearcher(serieRepository);

    return await serieSearcher.run();
}
