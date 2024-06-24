import { PaginatedResponse } from "@/contexts/shared/domain/PaginatedResponse";
import { Serie } from "./Serie";

export interface SerieRepository {
    matching(): Promise<PaginatedResponse<Serie>>;
    search(id: string): Promise<Serie | null>;
    create(serie: Serie): Promise<void>;
    update(serie: Serie): Promise<void>;
    delete(id: string): Promise<void>;
}
