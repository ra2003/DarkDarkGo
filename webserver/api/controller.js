const Aggregator = require('../Aggregation/Aggregator');
let Manager = require('../Management/Manager');

let test = 2


/*
/search?q=
/getsnippetsfordocids {id : [2131-dfadsf, 323-afa]}


*/

exports.handleQuery = (req, res) => {
    
    const queryString = req.query.q
    console.log("New query:", queryString)

    if (Manager.indexServers.empty || Manager.indexServers.map.length == 0 || Manager.indexServers.inversemap.length == 0) {
        returnError(res, "No index servers online")
    } else {
        // Make a request to the index servers, aggregate and prepare snippets

        Aggregator.queryIndexServerForDocIds(req.query.q, (success, error) => {
            
        })


        const results = Aggregator.queryIndexServerForDocIds(req.query.q)
        if (!results.success) return returnError(res, "Index servers not working. Please contact the administrator.")
        res.json({
            head: 'success',
            body: results.body
        });
    }
}

exports.handleHealth = (req, res) => {
    res.json(
        {
            'status': 'healthy'
        }
    )
}

/*
/searchid/:query

/searchsnippets/:id
*/
exports.fofhandler = (req, res) => {
    res.send('Invalid request');
}

returnError = (res, errormessage) => {
    res.json({
        head: 'error',
        message: errormessage
    });
}


//For testing only
// res.json({head: 'success',
// message: 
//     [
//         {
//             title: "How To Tie A Windsor Knot | Ties.com" + test++,
//             href: "https://www.ties.com/how-to-tie-a-tie/windsor",
//             desc: "The Windsor Knot Tying Instructions. Start with the wide end of the tie on the right and the small end on the left. Wide end over the small end to the left. Up into the neck loop from underneath. Down to the left. Around the back of the small end to the right. Up to the center, towards neck loop."
//         },
//         { 
//             title: "4 Ways to Tie a Tie - wikiHow",
//             href: "https://www.wikihow.com/Tie-a-Tie",
//             desc: "How to Tie a Tie. Have you graduated beyond the clip-on tie? Beginning with these helpful instructions, a sharp-looking tie, a mirror, and some patience, you can become an expert in tying your own fashionable knot. You have several options..."
//         },
//         {
//             title: "Brooks Brothers | How To Tie A Tie | Tie Knots",
//             href: "https://www.brooksbrothers.com/how-to-tie-a-tie/how-to-tie-a-tie,default,pg.html",
//             desc: "Watch our how to tie a tie videos on five classic knots including the Bow Tie knot, Windsor knot, Half Windsor knot, Pratt knot, and Four in Hand knot. The five tie knots every man should know."
//         }
//     ]
// }
// )