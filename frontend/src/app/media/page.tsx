import { useMedias } from "@/app/_hooks/useMedias";

export default async function MediaPage() {
    const medias = await useMedias();

    return (
        <div>
            <h1>Media</h1>
            <ul>
                {medias.items?.map((media) => (
                    <li key={media.getId()}>
                        <p>{media.getId() + " - " + media.getTitle()}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}
