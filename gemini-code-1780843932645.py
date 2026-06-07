import os

# Create an upgraded version of the portfolio in HTML/CSS with English content as requested.
# It includes dynamic placeholders for 20+ images organized across a clean Gallery, 
# dynamic projects, and life highlights sections, making it perfect for GitHub and Vercel.

html_v2_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prince AR Abdur Rahman | Founder & Entrepreneur</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            scroll-behavior: smooth;
        }
        .dark-gradient {
            background: linear-gradient(135deg, #090d16 0%, #0f172a 50%, #1e1b4b 100%);
        }
        .glass-premium {
            background: rgba(255, 255, 255, 0.02);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.07);
        }
        .glass-premium:hover {
            background: rgba(255, 255, 255, 0.05);
            border-color: rgba(56, 189, 248, 0.4);
            transform: translateY(-4px);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .text-glow {
            background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #090d16;
        }
        ::-webkit-scrollbar-thumb {
            background: #1e293b;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #38bdf8;
        }
    </style>
</head>
<body class="dark-gradient text-slate-100 min-h-screen antialiased">

    <header class="fixed top-0 left-0 w-full z-50 bg-slate-950/60 backdrop-blur-xl border-b border-slate-900">
        <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
            <a href="#" class="text-xl font-bold tracking-wider text-glow">PRINCE AR</a>
            <nav class="hidden md:flex space-x-8 text-sm font-medium text-slate-400">
                <a href="#home" class="hover:text-sky-400 transition-colors">Home</a>
                <a href="#about" class="hover:text-sky-400 transition-colors">About</a>
                <a href="#experience" class="hover:text-sky-400 transition-colors">Experience</a>
                <a href="#gallery" class="hover:text-sky-400 transition-colors">Gallery (20+)</a>
                <a href="#favorites" class="hover:text-sky-400 transition-colors">Interests</a>
                <a href="#contact" class="hover:text-sky-400 transition-colors">Contact</a>
            </nav>
            <a href="#contact" class="bg-gradient-to-r from-sky-500 to-indigo-500 hover:from-sky-600 hover:to-indigo-600 text-white px-5 py-2.5 rounded-xl text-xs font-semibold transition-all shadow-lg shadow-sky-500/10 hover:shadow-sky-500/20">Let's Connect</a>
        </div>
    </header>

    <section id="home" class="pt-36 pb-24 px-6 max-w-7xl mx-auto flex flex-col lg:flex-row items-center justify-between gap-16">
        <div class="flex-1 space-y-8 text-center lg:text-left">
            <div class="inline-flex items-center gap-2.5 bg-sky-500/10 border border-sky-500/20 px-4 py-1.5 rounded-full text-xs font-semibold text-sky-400 tracking-wide uppercase">
                <span class="w-2 h-2 rounded-full bg-sky-400 animate-pulse"></span> Future Millionaire Loading...
            </div>
            <h1 class="text-4xl sm:text-5xl md:text-6xl font-extrabold tracking-tight leading-tight">
                Building the Future <br>
                <span class="text-glow">Prince AR Abdur Rahman</span>
            </h1>
            <p class="text-lg text-slate-400 max-w-xl mx-auto lg:mx-0 font-light leading-relaxed">
                Visionary Entrepreneur and the Founder of <strong class="text-slate-200 font-semibold">Nexvora Labs</strong>. Driven by ambition, self-respect, and cutting-edge innovations to change the paradigm.
            </p>
            <div class="flex flex-wrap justify-center lg:justify-start gap-4">
                <a href="#contact" class="bg-white text-slate-950 px-7 py-3.5 rounded-xl font-medium hover:bg-slate-200 transition shadow-lg shadow-white/5">Get In Touch</a>
                <a href="#gallery" class="bg-slate-900/60 hover:bg-slate-800 text-slate-200 px-7 py-3.5 rounded-xl font-medium transition border border-slate-800">View Showcase</a>
            </div>
        </div>
        
        <div class="flex-1 grid grid-cols-12 gap-4 max-w-md lg:max-w-none w-full">
            <div class="col-span-8 relative group overflow-hidden rounded-2xl border border-slate-800 shadow-2xl h-80">
                <img src="img1.jpg" alt="Profile Picture Main" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" onerror="this.src='https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=600&q=80'">
                <div class="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-slate-950 to-transparent text-xs text-slate-300">Profile Focus</div>
            </div>
            <div class="col-span-4 grid grid-rows-2 gap-4 h-80">
                <div class="relative group overflow-hidden rounded-xl border border-slate-800 shadow-xl">
                    <img src="img2.jpg" alt="Bachelor Point Vibe" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" onerror="this.src='https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=300&q=80'">
                </div>
                <div class="relative group overflow-hidden rounded-xl border border-slate-800 shadow-xl">
                    <img src="img3.jpg" alt="Tetulia Travel" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" onerror="this.src='https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&w=300&q=80'">
                </div>
            </div>
        </div>
    </section>

    <section id="about" class="py-24 px-6 max-w-7xl mx-auto border-t border-slate-900/60">
        <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
            <h2 class="text-3xl font-bold tracking-tight">The Core Profile</h2>
            <p class="text-slate-400 text-sm">"Self respect is more important than feelings." — Integrity over everything.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="glass-premium p-8 rounded-2xl space-y-5 transition-all">
                <div class="w-12 h-12 rounded-xl bg-sky-500/10 flex items-center justify-center text-sky-400 text-lg">
                    <i class="fa-solid fa-crown"></i>
                </div>
                <h3 class="font-bold text-xl">Leadership & Status</h3>
                <p class="text-sm text-slate-400 leading-relaxed">
                    Founder and executive director driving conceptual pipelines at <span class="text-sky-400">Nexvora Labs</span>. Overseeing technological products and team management since launch.
                </p>
            </div>
            <div class="glass-premium p-8 rounded-2xl space-y-5 transition-all">
                <div class="w-12 h-12 rounded-xl bg-indigo-500/10 flex items-center justify-center text-indigo-400 text-lg">
                    <i class="fa-solid fa-graduation-cap"></i>
                </div>
                <h3 class="font-bold text-xl">Education Foundation</h3>
                <p class="text-sm text-slate-400 leading-relaxed">
                    Alumni/Student of <span class="text-indigo-400">Sunflower school and college saidpur, Nilphamari</span>. Academic excellence mixed with self-taught enterprise knowledge.
                </p>
            </div>
            <div class="glass-premium p-8 rounded-2xl space-y-5 transition-all">
                <div class="w-12 h-12 rounded-xl bg-purple-500/10 flex items-center justify-center text-purple-400 text-lg">
                    <i class="fa-solid fa-globe"></i>
                </div>
                <h3 class="font-bold text-xl">Roots & Linguals</h3>
                <p class="text-sm text-slate-400 leading-relaxed">
                    Based out of <span class="text-purple-400">Rangpur City</span>. Polyglot mindset with fluent communication abilities across English, Bengali, and Hindi languages.
                </p>
            </div>
        </div>
    </section>

    <section id="experience" class="py-24 px-6 max-w-4xl mx-auto border-t border-slate-900/60">
        <h2 class="text-3xl font-bold tracking-tight text-center mb-16">Work & Business Milestones</h2>
        <div class="relative border-l-2 border-slate-800 pl-8 space-y-12 ml-4">
            <div class="relative">
                <div class="absolute -left-[41px] top-1.5 w-5 h-5 rounded-full bg-sky-400 border-4 border-slate-950 shadow-md"></div>
                <span class="text-xs font-bold uppercase tracking-wider text-sky-400 bg-sky-400/10 px-3 py-1 rounded-full">March 2026 - Present</span>
                <h3 class="text-2xl font-bold mt-3 text-white">Founder & Visionary</h3>
                <h4 class="text-slate-400 text-md font-medium mt-1">Nexvora Labs</h4>
                <p class="text-sm text-slate-400 mt-3 leading-relaxed">
                    Pioneering operational tasks, project system development, and branding strategies. Guiding the roadmap to establish Nexvora Labs as a leading industrial venture.
                </p>
            </div>
        </div>
    </section>

    <section id="gallery" class="py-24 px-6 max-w-7xl mx-auto border-t border-slate-900/60">
        <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
            <h2 class="text-3xl font-bold tracking-tight">Visual Journey <span class="text-glow">(20+ Portfolio Captures)</span></h2>
            <p class="text-slate-400 text-sm">A comprehensive collection of moments, locations (Tetulia, Saidpur, Rangpur), and life experiences.</p>
        </div>
        
        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
            
            <div class="relative group overflow-hidden rounded-xl border border-slate-800/80 bg-slate-900 aspect-square">
                <img src="img4.jpg" alt="Saidpur City Look" class="w-full h-full object-cover transition duration-500 group-hover:scale-110" onerror="this.src='https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=400&q=80'">
                <div class="absolute inset-0 bg-slate-950/70 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center p-4 text-center">
                    <span class="text-xs font-medium text-slate-200">Saidpur City Shoot</span>
                </div>
            </div>
            <div class="relative group overflow-hidden rounded-xl border border-slate-800/80 bg-slate-900 aspect-square">
                <img src="img5.jpg" alt="Bachelor Point Aesthetic" class="w-full h-full object-cover transition duration-500 group-hover:scale-110" onerror="this.src='https://images.unsplash.com/photo-1511556532299-8f662fc26c06?auto=format&fit=crop&w=400&q=80'">
                <div class="absolute inset-0 bg-slate-950/70 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center p-4 text-center">
                    <span class="text-xs font-medium text-slate-200">Bachelor Point Vibe</span>
                </div>
            </div>
            <div class="relative group overflow-hidden rounded-xl border border-slate-800/80 bg-slate-900 aspect-square">
                <img src="img6.jpg" alt="Tetulia Heart Frame" class="w-full h-full object-cover transition duration-500 group-hover:scale-110" onerror="this.src='https://images.unsplash.com/photo-1473448912268-2022ce9509d8?auto=format&fit=crop&w=400&q=80'">
                <div class="absolute inset-0 bg-slate-950/70 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center p-4 text-center">
                    <span class="text-xs font-medium text-slate-200">Tetulia Travel Diary</span>
                </div>
            </div>
            <div class="relative group overflow-hidden rounded-xl border border-slate-800/80 bg-slate-900 aspect-square">
                <img src="img7.jpg" alt="Silent Heart Moment" class="w-full h-full object-cover transition duration-500 group-hover:scale-110" onerror="this.src='https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=400&q=80'">
                <div class="absolute inset-0 bg-slate-950/70 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center p-4 text-center">
                    <span class="text-xs font-medium text-slate-200">Silent Heart Shoot</span>
                </div>
            </div>

            <div class="relative group overflow-hidden rounded-xl border border-slate-800/80 bg-slate-900 aspect-square">
                <img src="img8.jpg" alt="Tea Lover Chronicles" class="w-full h-full object-cover transition duration-500 group-hover:scale-110" onerror="this.src='https://images.unsplash.com/photo-1544787219-7f47ccb76574?auto=format&fit=crop&w=400&q=80'">
                <div class="absolute inset-0 bg-slate-950/70 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center p-4 text-center">
                    <span class="text-xs font-medium text-slate-200">Tea over Fake People</span>
                </div>
            </div>
            <div class="relative group overflow-hidden rounded-xl border border-slate-800/80 bg-slate-900 aspect-square">
                <img src="img9.jpg" alt="Alhamdulillah Post Visual" class="w-full h-full object-cover transition duration-500 group-hover:scale-110" onerror="this.src='https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=400&q=80'">
                <div class="absolute inset-0 bg-slate-950/70 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center p-4 text-center">
                    <span class="text-xs font-medium text-slate-200">Alhamdulillah for everything</span>
                </div>
            </div>
            <div class="relative group overflow-hidden rounded-xl border border-slate-800/80 bg-slate-900 aspect-square">
                <img src="img10.jpg" alt="Formal Event Pose" class="w-full h-full object-cover transition duration-500 group-hover:scale-110" onerror="this.src='https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?auto=format&fit=crop&w=400&q=80'">
                <div class="absolute inset-0 bg-slate-950/70 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center p-4 text-center">
                    <span class="text-xs font-medium text-slate-200">Saidpur Campus Visual</span>
                </div>
            </div>
            <div class="relative group overflow-hidden rounded-xl border border-slate-800/80 bg-slate-900 aspect-square">
                <img src="img11.jpg" alt="Intezar Session" class="w-full h-full object-cover transition duration-500 group-hover:scale-110" onerror="this.src='https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=80'">
                <div class="absolute inset-0 bg-slate-950/70 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center p-4 text-center">
                    <span class="text-xs font-medium text-slate-200">Intezar Vibe Box</span>
                </div>
            </div>

            <div class="relative group overflow-hidden rounded-xl border border-slate-800/80 bg-slate-900 aspect-square">
                <img src="img12.jpg" alt="Rangpur City Lifestyle" class="w-full h-full object-cover transition duration-500 group-hover:scale-110" onerror="this.src='https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=400&q=80'">
                <div class="absolute inset-0 bg-slate-950/70 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center p-4 text-center">
                    <span class="text-xs font-medium text-slate-200">Rangpur Hub Session</span>
                </div>
            </div>
            <div class="relative group overflow-hidden rounded-xl border border-slate-800/80 bg-slate-900 aspect-square">
                <img src="img13.jpg" alt="Nexvora Operations" class="w-full h-full object-cover transition duration-500 group-hover:scale-110" onerror="this.src='https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=400&q=80'">
                <div class="absolute inset-0 bg-slate-950/70 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center p-4 text-center">
                    <span class="text-xs font-medium text-slate-200">Nexvora Planning Meet</span>
                </div>
            </div>
            <div class="relative group overflow-hidden rounded-xl border border-slate-800/80 bg-slate-900 aspect-square">
                <img src="img14.jpg" alt="Travel Landscape" class="w-full h-full object-cover transition duration-500 group-hover:scale-110" onerror="this.src='https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=400&q=80'">
                <div class="absolute inset-0 bg-slate-950/70 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center p-4 text-center">
                    <span class="text-xs font-medium text-slate-200">Wanderlust Exploring</span>
                </div>
            </div>
            <div class="relative group overflow-hidden rounded-xl border border-slate-800/80 bg-slate-900 aspect-square">
                <img src="img15.jpg" alt="Gaming Setup Vibe" class="w-full h-full object-cover transition duration-500 group-hover:scale-110" onerror="this.src='https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=400&q=80'">
                <div class="absolute inset-0 bg-slate-950/70 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center p-4 text-center">
                    <span class="text-xs font-medium text-slate-200">Esports Hub Vibe</span>
                </div>
            </div>
            <div class="relative group overflow-hidden rounded-xl border border-slate-800/80 bg-slate-900 aspect-square">
                <img src="img16.jpg" alt="Tech Conference" class="w-full h-full object-cover transition duration-500 group-hover:scale-110" onerror="this.src='https://images.unsplash.com/photo-1515187029135-18ee286d815b?auto=format&fit=crop&w=400&q=80'">
                <div class="absolute inset-0 bg-slate-950/70 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center p-4 text-center">
                    <span class="text-xs font-medium text-slate-200">Startup Network</span>
                </div>
            </div>
            <div class="relative group overflow-hidden rounded-xl border border-slate-800/80 bg-slate-900 aspect-square">
                <img src="img17.jpg" alt="Chill Sunset View" class="w-full h-full object-cover transition duration-500 group-hover:scale-110" onerror="this.src='https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=400&q=80'">
                <div class="absolute inset-0 bg-slate-950/70 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center p-4 text-center">
                    <span class="text-xs font-medium text-slate-200">Sunset Reflection</span>
                </div>
            </div>
            <div class="relative group overflow-hidden rounded-xl border border-slate-800/80 bg-slate-900 aspect-square">
                <img src="img18.jpg" alt="Coffee / Tea Session" class="w-full h-full object-cover transition duration-500 group-hover:scale-110" onerror="this.src='https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=400&q=80'">
                <div class="absolute inset-0 bg-slate-950/70 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center p-4 text-center">
                    <span class="text-xs font-medium text-slate-200">Cafeteria Lounge</span>
                </div>
            </div>
            <div class="relative group overflow-hidden rounded-xl border border-slate-800/80 bg-slate-900 aspect-square">
                <img src="img19.jpg" alt="Football Night" class="w-full h-full object-cover transition duration-500 group-hover:scale-110" onerror="this.src='https://images.unsplash.com/photo-1508098682722-e99c43a406b2?auto=format&fit=crop&w=400&q=80'">
                <div class="absolute inset-0 bg-slate-950/70 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center p-4 text-center">
                    <span class="text-xs font-medium text-slate-200">Matchday Vibe</span>
                </div>
            </div>
            <div class="relative group overflow-hidden rounded-xl border border-slate-800/80 bg-slate-900 aspect-square">
                <img src="img20.jpg" alt="Urban Street Walk" class="w-full h-full object-cover transition duration-500 group-hover:scale-110" onerror="this.src='https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=400&q=80'">
                <div class="absolute inset-0 bg-slate-950/70 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center p-4 text-center">
                    <span class="text-xs font-medium text-slate-200">Street Vibe Out</span>
                </div>
            </div>
            <div class="relative group overflow-hidden rounded-xl border border-slate-800/80 bg-slate-900 aspect-square">
                <img src="img21.jpg" alt="Inspirational Office Space" class="w-full h-full object-cover transition duration-500 group-hover:scale-110" onerror="this.src='https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=400&q=80'">
                <div class="absolute inset-0 bg-slate-950/70 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center p-4 text-center">
                    <span class="text-xs font-medium text-slate-200">Future Boardroom</span>
                </div>
            </div>
            <div class="relative group overflow-hidden rounded-xl border border-slate-800/80 bg-slate-900 aspect-square">
                <img src="img22.jpg" alt="Strategic Mindset" class="w-full h-full object-cover transition duration-500 group-hover:scale-110" onerror="this.src='https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=400&q=80'">
                <div class="absolute inset-0 bg-slate-950/70 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center p-4 text-center">
                    <span class="text-xs font-medium text-slate-200">Deep Work Vibe</span>
                </div>
            </div>
            <div class="relative group overflow-hidden rounded-xl border border-slate-800/80 bg-slate-900 aspect-square">
                <img src="img23.jpg" alt="Victory Celebration" class="w-full h-full object-cover transition duration-500 group-hover:scale-110" onerror="this.src='https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=400&q=80'">
                <div class="absolute inset-0 bg-slate-950/70 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center p-4 text-center">
                    <span class="text-xs font-medium text-slate-200">Nature Summit Achieved</span>
                </div>
            </div>
            <div class="relative group overflow-hidden rounded-xl border border-slate-800/80 bg-slate-900 aspect-square">
                <img src="img24.jpg" alt="Final Showcase Capture" class="w-full h-full object-cover transition duration-500 group-hover:scale-110" onerror="this.src='https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=400&q=80'">
                <div class="absolute inset-0 bg-slate-950/70 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center p-4 text-center">
                    <span class="text-xs font-medium text-slate-200">The Next Gen Goal</span>
                </div>
            </div>

        </div>
    </section>

    <section id="favorites" class="py-24 px-6 max-w-7xl mx-auto border-t border-slate-900/60">
        <h2 class="text-3xl font-bold tracking-tight text-center mb-16">Interests & Entertainment Mix</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            <div class="glass-premium p-6 rounded-2xl">
                <h3 class="font-bold text-sm text-slate-300 mb-4 flex items-center gap-2">
                    <i class="fa-solid fa-music text-pink-400"></i> Top Soundtrack
                </h3>
                <div class="bg-slate-950/40 p-4 rounded-xl border border-slate-800/50">
                    <p class="text-sm font-semibold text-slate-200">Long Distance Love</p>
                    <p class="text-xs text-slate-500 mt-0.5">Coke Studio Bangla</p>
                </div>
            </div>
            <div class="glass-premium p-6 rounded-2xl">
                <h3 class="font-bold text-sm text-slate-300 mb-4 flex items-center gap-2">
                    <i class="fa-solid fa-tv text-sky-400"></i> TV & Anime Series
                </h3>
                <ul class="space-y-2.5 text-xs text-slate-400">
                    <li class="flex items-center gap-2"><i class="fa-solid fa-circle-play text-sky-500"></i> Attack On Titan</li>
                    <li class="flex items-center gap-2"><i class="fa-solid fa-circle-play text-sky-500"></i> Naruto Shippuden</li>
                    <li class="flex items-center gap-2"><i class="fa-solid fa-circle-play text-sky-500"></i> Money Heist</li>
                </ul>
            </div>
            <div class="glass-premium p-6 rounded-2xl">
                <h3 class="font-bold text-sm text-slate-300 mb-4 flex items-center gap-2">
                    <i class="fa-solid fa-film text-purple-400"></i> Cinematic Picks
                </h3>
                <ul class="space-y-2.5 text-xs text-slate-400">
                    <li class="flex items-center gap-2"><i class="fa-solid fa-clapperboard text-purple-500"></i> 3 Idiots</li>
                    <li class="flex items-center gap-2"><i class="fa-solid fa-clapperboard text-purple-500"></i> Avengers: Endgame</li>
                </ul>
            </div>
            <div class="glass-premium p-6 rounded-2xl">
                <h3 class="font-bold text-sm text-slate-300 mb-4 flex items-center gap-2">
                    <i class="fa-solid fa-gamepad text-emerald-400"></i> Esports & Sports
                </h3>
                <div class="space-y-3.5">
                    <div class="flex flex-wrap gap-1">
                        <span class="text-[10px] bg-slate-800/80 px-2 py-0.5 rounded text-slate-300">Clash of Clans</span>
                        <span class="text-[10px] bg-slate-800/80 px-2 py-0.5 rounded text-slate-300">Free Fire</span>
                        <span class="text-[10px] bg-slate-800/80 px-2 py-0.5 rounded text-slate-300">PUBG Mobile</span>
                    </div>
                    <div class="text-xs text-slate-400 border-t border-slate-800/60 pt-2 space-y-1">
                        <p><i class="fa-solid fa-star text-amber-400 mr-1"></i> Idol: <span class="text-slate-200">Leo Messi</span></p>
                        <p><i class="fa-solid fa-shield-halved text-sky-400 mr-1"></i> Teams: <span class="text-slate-200">Argentina / Barcelona</span></p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="contact" class="py-24 px-6 max-w-4xl mx-auto border-t border-slate-900/60 text-center space-y-8">
        <h2 class="text-3xl font-bold tracking-tight">Let's Create Something Great</h2>
        <p class="text-slate-400 max-w-md mx-auto text-sm leading-relaxed">
            Interested in partnering up, discussing venture options, or tracking my journey? Catch me on social platforms.
        </p>
        <div class="flex justify-center gap-5 pt-4">
            <a href="https://instagram.com/ur___abdur___rahman__20008" target="_blank" class="w-14 h-14 rounded-2xl bg-gradient-to-tr from-amber-500 via-pink-500 to-purple-600 flex items-center justify-center text-white text-2xl hover:scale-110 transition shadow-lg shadow-pink-500/10">
                <i class="fa-brands fa-instagram"></i>
            </a>
            <a href="#" class="w-14 h-14 rounded-2xl bg-blue-600 flex items-center justify-center text-white text-2xl hover:scale-110 transition shadow-lg shadow-blue-600/10">
                <i class="fa-brands fa-facebook"></i>
            </a>
            <a href="#" class="w-14 h-14 rounded-2xl bg-red-600 flex items-center justify-center text-white text-2xl hover:scale-110 transition shadow-lg shadow-red-600/10">
                <i class="fa-brands fa-youtube"></i>
            </a>
            <a href="#" class="w-14 h-14 rounded-2xl bg-slate-800 flex items-center justify-center text-white text-2xl hover:scale-110 transition shadow-lg shadow-slate-800/10">
                <i class="fa-brands fa-github"></i>
            </a>
        </div>
    </section>

    <footer class="py-10 text-center text-xs text-slate-500 border-t border-slate-950 bg-slate-950/50">
        <p>© 2026 Prince AR Abdur Rahman. Powered by Nexvora Labs. All Rights Reserved.</p>
    </footer>

</body>
</html>
"""

with open("index-v2.html", "w", encoding="utf-8") as file:
    file.write(html_v2_content)

print("index-v2.html updated version created successfully.")