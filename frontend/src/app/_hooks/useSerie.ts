import { SerieFinder } from "@/contexts/backoffice/series/application/SerieFinder";
import { HTTPSerieRepository } from "@/contexts/backoffice/series/infrastructure/persistence/http/HTTPSerieRepository";

export async function useSerie(id: string) {
    const serieRepository = new HTTPSerieRepository();
    const serieFinder = new SerieFinder(serieRepository);

    return await serieFinder.run(id);
}
