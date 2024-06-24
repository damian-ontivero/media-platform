export type PaginatedResponse<T> = {
    pageSize: number;
    pageNumber: number;
    totalPages: number;
    items: T[];
};
