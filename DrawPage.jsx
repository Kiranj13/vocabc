export default function DrawPage({ onSubmit }) {
const speak = (text) => {
const utter = new SpeechSynthesisUtterance(text);
window.speechSynthesis.speak(utter);
};
return (
<div className="p-6 text-center">
<div className="flex justify-center items-center gap-8 mb-10">
<div className="text-2xl font-semibold">Apple</div>
<button onClick={() => speak('Apple')} className="text-2xl">🔊</button>
<div className="text-2xl font-semibold">ఆ
ి
</div>

<button onClick={() => speak('ఆ
ి
')} className="text-2xl">🔊</button>

</div>
<div className="w-72 h-48 border-2 border-dashed border-gray-400 mx-auto mb-10 flex
items-center justify-center">
Drawing Area
</div>
<button
onClick={onSubmit}
className="bg-green-500 text-white px-6 py-2 rounded-lg hover:bg-green-600"
>
Submit
</button>
</div>
);
}
