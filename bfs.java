import java.util.*;

import org.w3c.dom.Node;

public class bfs {
   public static void main(String[] args) {

   }

   public static int bfs(Node root, Node target) {
      Queue<Node> queue = new LinkedList<>();
      Set<Node> seen = new HashSet<>();
      int step = 0;

      queue.add(root);

      while (!queue.isEmpty()) {
         Node curr = queue.poll();

         if (curr == target) {
            return step;
         }
         if (!seen.contains(curr)) {
            seen.add(curr);
         }

         for (Node adjacent : curr.adjacent) {
            if (!seen.contains(adjacent)) {
               queue.add(adjacent);
            }
         }
         step++;
         
      }

      return -1;
   }
}