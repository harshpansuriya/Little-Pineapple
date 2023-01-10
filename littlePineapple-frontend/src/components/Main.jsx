import thinking from '../assets/img/thinking.jpg'
import client from '../assets/img/client.jpg'
import skiller from '../assets/img/skiller.jpg'

export default function Main() {
    return (
        <div className='mt-10 flex justify-between'>
            <div className='border-4 flex-1 flex-col m-4 p-4 rounded-xl'>
                <p className='text-xl font-bold'>Why are we?</p>
                <img src={thinking} alt="Downloaded from Vecteezy.com" className='w-96'/>
            </div>
            <div className='flex flex-col flex-1 '>
                <div className='flex border-4 m-4 p-4 rounded-xl justify-around'>
                    <div>
                        <p className='text-xl font-bold'>Find perfect person for your perfect work!</p>
                        <button >Find Out</button>
                    </div>
                    <img src={client} alt="Downloaded from Vecteezy.com" className='w-64'/>
                </div>
                <div className='flex border-4 m-4 p-4 rounded-xl'>
                    <p className='text-xl font-bold'>Register and get your skill job.</p>
                    <img src={skiller} alt="Downloaded from Vecteezy.com" className='w-64'/>
                </div>
            </div>
        </div>
    )
}