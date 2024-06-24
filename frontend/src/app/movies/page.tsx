"use client";
import { useMovies } from "../_hooks/useMovies";

export default async function MoviePage() {
    const movies = await useMovies();

    return (
        <div>
            <h1>Movie</h1>
            <ul>
                {movies.items?.map((movie) => (
                    <li key={movie.getId()}>
                        <p>{movie.getId() + " - " + movie.getTitle()}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}
