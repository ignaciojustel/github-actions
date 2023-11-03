public class HelloWorld {
    public static void main(String[] args) {
        String username = System.getenv("USERNAME");
        
        System.out.println("Bienvenido " + username + ".\nHola, Mundo!");
    }
}
