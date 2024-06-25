"use client";
import { useSeries } from "@/app/backoffice/_hooks/series/useSeries";

export default function SeriePage() {
    const { data, isLoading } = useSeries();

    if (isLoading) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>Serie</h1>
            <ul>
                {data?.items?.map((serie) => (
                    <li key={serie.getId()}>
                        <p>{serie.getId() + " - " + serie.getTitle()}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}
