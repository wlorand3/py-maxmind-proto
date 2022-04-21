import asyncio
import geoip2.webservice

import data.ip_data as data


async def main():

    async with geoip2.webservice.AsyncClient(682306, '5KiqWEPTVo5HE7j4', host='geolite.info') as client:
        response = await client.city(data.sample_ip_address)
        # TODO: loop thru and return the same object as the db script for DEMO
        # i remember why loop data not here === multiple async client calls
        print(response.city.name)
        print(response.location.latitude)
        print(response.location.longitude)

asyncio.run(main())
