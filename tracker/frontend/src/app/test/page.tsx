export default function Page() {
  return (
    <div className="grid grid-cols-2 items-center justify-center">
      <iframe
        className="h-[90vh] w-full"
        src="/torrent-page"
        title="Torrent Client 1"
      />
      <iframe
        className="h-[90vh] w-full"
        src="/torrent-page"
        title="Torrent Client 2"
      />
    </div>
  );
}
