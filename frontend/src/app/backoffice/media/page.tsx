"use client";
import { useMedias } from "./_hooks/useMedias";

export default function MediaPage() {
    const { data, isLoading } = useMedias();

    if (isLoading) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>Media</h1>
            <ul>
                {data?.items.map((media) => (
                    <li key={media.getId()}>
                        <p>{media.getId() + " - " + media.getTitle()}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}
