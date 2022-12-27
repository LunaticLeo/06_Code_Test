package test_java_eclipse;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class test {

	public static long[] main(long[][] chunks) {
		// TODO Auto-generated method stub
		ArrayList<Long> res = new ArrayList<Long>();
		res.add(0L);

		ArrayList<long[]> actual_chunks = new ArrayList<long[]>();

		boolean append = true;

		// curr_chunk chunks[i]
		// prev_chunk actual_chunks.get(j)
		for (int i = 0; i < chunks.length; i++) {
			long size = chunks[i][1] - chunks[i][0] + 1;

			long left, right;
			for (int j = 0; j < actual_chunks.size(); j++) {
				if (chunks[i][0] >= actual_chunks.get(j)[0] && chunks[i][1] <= actual_chunks.get(j)[1]) {
					size = 0L;
					break;
				} else if (actual_chunks.get(j)[0] <= chunks[i][0] && chunks[i][0] <= actual_chunks.get(j)[1]
						&& chunks[i][1] > actual_chunks.get(j)[1]) {
					size -= actual_chunks.get(j)[1] - chunks[i][0] + 1;
					left = actual_chunks.get(j)[1] + 1;
					right = chunks[i][1];
				} else if (chunks[i][0] < actual_chunks.get(j)[0] && actual_chunks.get(j)[0] <= chunks[i][1]
						&& chunks[i][1] <= actual_chunks.get(j)[1]) {
					size -= chunks[i][1] - actual_chunks.get(j)[0] + 1;
					left = chunks[i][0];
					right = actual_chunks.get(j)[0] - 1;
				} else if (chunks[i][0] < actual_chunks.get(j)[0] && chunks[i][1] > actual_chunks.get(j)[1]) {
					size -= actual_chunks.get(j)[1] - actual_chunks.get(j)[0] + 1;
					actual_chunks.set(j, chunks[i]);
				}
			}
			
			actual_chunks.add(chunks[i]);
			res.add(res.get(res.size()-1) + size);
		}
		
		res.remove(0);
		
		long[] output = new long[res.size()];
		for(int i=0;i<output.length;i++) {
			output[i] = res.get(i);
		}
		return output;

	}

}
