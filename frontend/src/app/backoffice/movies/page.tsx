"use client";
import { useMovies } from "@/app/backoffice/_hooks/movies/useMovies";

export default function MoviePage() {
    const { data, isLoading } = useMovies();

    if (isLoading) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>Movie</h1>
            <ul>
                {data?.items?.map((movie) => (
                    <li key={movie.getId()}>
                        <p>{movie.getId() + " - " + movie.getTitle()}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}
