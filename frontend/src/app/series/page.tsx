"use client";
import { useSeries } from "../_hooks/useSeries";

export default async function SeriePage() {
    const series = await useSeries();

    return (
        <div>
            <h1>Serie</h1>
            <ul>
                {series.items?.map((serie) => (
                    <li key={serie.getId()}>
                        <p>{serie.getId() + " - " + serie.getTitle()}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}
