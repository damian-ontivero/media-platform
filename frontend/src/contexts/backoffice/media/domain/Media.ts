export type MediaParams = {
    id: string;
    title: string;
    size: number;
    duration: number;
    path: string;
};

export class Media {
    private readonly id: string;
    private readonly title: string;
    private readonly size: number;
    private readonly duration: number;
    private readonly path: string;

    constructor({ id, title, size, duration, path }: MediaParams) {
        this.id = id;
        this.title = title;
        this.size = size;
        this.duration = duration;
        this.path = path;
    }

    getId(): string {
        return this.id;
    }

    getTitle(): string {
        return this.title;
    }

    getSize(): number {
        return this.size;
    }

    getDuration(): number {
        return this.duration;
    }

    getPath(): string {
        return this.path;
    }
}
