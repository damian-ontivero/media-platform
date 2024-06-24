import { Movie } from "./Movie";

export type PaginatedResponse<T> = {
    pageSize: number;
    pageNumber: number;
    totalPages: number;
    items: T[];
};

export interface MovieRepository {
    matching(): Promise<PaginatedResponse<Movie>>;
    search(id: string): Promise<Movie | null>;
    create(movie: Movie): Promise<void>;
    update(movie: Movie): Promise<void>;
    delete(id: string): Promise<void>;
}
