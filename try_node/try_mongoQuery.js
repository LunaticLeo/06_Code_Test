const { MongoClient } = require('mongodb');
// or as an es module:
// import { MongoClient } from 'mongodb'

// Connection URL
const url = 'mongodb://localhost:27017';
const client = new MongoClient(url);

// Database Name
const dbName = 'Taskoo';

async function main() {
    // Use connect method to connect to the server
    await client.connect();
    console.log('Connected successfully to server');
    const db = client.db(dbName);
    const col = db.collection('buckets');

    // the following code examples can be pasted here...
    const data = await col.aggregate(
        [
            {
                '$match': {
                    '_id': '464fc3d8-b3f1-4414-83f4-92671a1e88ef'
                }
            }, {
                '$project': {
                    'userProjects': {
                        '$concatArrays': [
                            '$projects.pending', '$projects.processing', '$projects.testing', '$projects.done'
                        ]
                    }, 
                    '_id': 0
                }
            }, {
                '$lookup': {
                    'from': 'projects', 
                    'localField': 'userProjects', 
                    'foreignField': '_id', 
                    'as': 'userProjectsDetails'
                }
            }
        ]
    ).toArray();

    console.dir(data, { depth: null });
    client.close();
    return 'done.';
}

main();