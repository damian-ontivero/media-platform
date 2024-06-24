import { Serie } from "./Serie";

export type PaginatedResponse<T> = {
    pageSize: number;
    pageNumber: number;
    totalPages: number;
    items: T[];
};

export interface SerieRepository {
    matching(): Promise<PaginatedResponse<Serie>>;
    search(id: string): Promise<Serie | null>;
    create(serie: Serie): Promise<void>;
    update(serie: Serie): Promise<void>;
    delete(id: string): Promise<void>;
}
