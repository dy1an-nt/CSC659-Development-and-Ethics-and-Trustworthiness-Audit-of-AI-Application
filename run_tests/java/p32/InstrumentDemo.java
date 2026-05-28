public class InstrumentDemo {
    interface Playable {
        void play();
        default String getType() { return "Unknown Instrument"; }
    }
    static class Guitar implements Playable {
        private String brand;
        public Guitar(String brand) { this.brand = brand; }
        @Override
        public void play() { System.out.println(brand + " Guitar: Strumming chords..."); }
        @Override
        public String getType() { return "String Instrument"; }
    }
    static class Piano implements Playable {
        @Override
        public void play() { System.out.println("Piano: Playing a melody..."); }
    }
    public static void main(String[] args) {
        Playable[] instruments = { new Guitar("Fender"), new Piano() };
        for (Playable instrument : instruments) {
            instrument.play();
            System.out.println("  Type: " + instrument.getType());
        }
    }
}
