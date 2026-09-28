import {
  BarChart3,
  Building2,
  Contact,
  Database,
  FileText,
  Users,
} from "lucide-react";

const nodes = {
  topLeft: [
    {
      label: "Contacts",
      icon: Contact,
      className: "left-[7%] top-[18%]",
    },
    {
      label: "Leads",
      icon: Users,
      className: "left-[16%] top-[31%]",
    },
    {
      label: "Companies",
      icon: Building2,
      className: "left-[5%] top-[40%]",
    },
  ],

  topRight: [
    {
      label: "Revenue",
      icon: BarChart3,
      className: "right-[8%] top-[18%]",
    },
    {
      label: "Analytics",
      icon: BarChart3,
      className: "right-[16%] top-[31%]",
    },
    {
      label: "AI Insights",
      icon: FileText,
      className: "right-[5%] top-[41%]",
    },
  ],

  bottomLeft: [
    {
      label: "Qualified",
      icon: Users,
      className: "left-[7%] bottom-[27%]",
    },
    {
      label: "Proposal",
      icon: FileText,
      className: "left-[17%] bottom-[15%]",
    },
  ],

  bottomRight: [
    {
      label: "Customers",
      icon: Users,
      className: "right-[20%] bottom-[25%]",
    },
    {
      label: "Activities",
      icon: FileText,
      className: "right-[7%] bottom-[16%]",
    },
  ],
};

function DataNode({ label, icon: Icon, className }) {
  return (
    <div
      className={`
        absolute
        ${className}
        hidden
        items-center
        gap-2
        rounded-full
        border
        border-white/90
        bg-white/70
        px-3
        py-2
        shadow-[0_8px_25px_rgba(14,165,233,0.08)]
        backdrop-blur-md
        transition-all
        duration-500
        lg:flex
      `}
    >
      <span className="flex h-5 w-5 items-center justify-center rounded-full bg-cyan-50">
        <Icon
          className="h-3 w-3 text-sky-500"
          strokeWidth={2}
        />
      </span>

      <span className="whitespace-nowrap text-[10px] font-medium tracking-wide text-slate-500">
        {label}
      </span>
    </div>
  );
}

export function AuthBackground() {
  return (
    <div
      aria-hidden="true"
      className="pointer-events-none absolute inset-0 overflow-hidden"
    >
      {/* =====================================================
          BASE AMBIENT LIGHT
      ====================================================== */}

      <div
        className="
          absolute
          left-1/2
          top-1/2
          h-136
          w-136
          -translate-x-1/2
          -translate-y-1/2
          rounded-full
          bg-cyan-300/10
          blur-[120px]
          sm:h-168
          sm:w-2xl
        "
      />

      <div
        className="
          absolute
          -right-40
          -top-40
          h-120
          w-120
          rounded-full
          bg-sky-200/20
          blur-[110px]
        "
      />

      <div
        className="
          absolute
          -bottom-40
          -left-40
          h-112
          w-md
          rounded-full
          bg-cyan-100/30
          blur-[100px]
        "
      />

      {/* =====================================================
          DOT MATRIX
      ====================================================== */}

      <div
        className="
          absolute
          inset-0
          opacity-60
        "
        style={{
          backgroundImage:
            "radial-gradient(circle, rgba(56,189,248,0.34) 1px, transparent 1px)",
          backgroundSize: "16px 16px",
          maskImage:
            "radial-gradient(ellipse 75% 75% at center, black 20%, transparent 85%)",
          WebkitMaskImage:
            "radial-gradient(ellipse 75% 75% at center, black 20%, transparent 85%)",
        }}
      />

      {/* =====================================================
          DATA CONNECTION NETWORK
      ====================================================== */}

      <svg
        className="
          absolute
          inset-0
          h-full
          w-full
        "
        viewBox="0 0 1000 800"
        preserveAspectRatio="none"
      >
        <defs>
          <linearGradient
            id="dataLine"
            x1="0"
            y1="0"
            x2="1"
            y2="1"
          >
            <stop
              offset="0%"
              stopColor="#38bdf8"
              stopOpacity="0.05"
            />

            <stop
              offset="50%"
              stopColor="#38bdf8"
              stopOpacity="0.42"
            />

            <stop
              offset="100%"
              stopColor="#38bdf8"
              stopOpacity="0.08"
            />
          </linearGradient>

          <filter id="softGlow">
            <feGaussianBlur
              stdDeviation="2"
              result="blur"
            />

            <feMerge>
              <feMergeNode in="blur" />
              <feMergeNode in="SourceGraphic" />
            </feMerge>
          </filter>
        </defs>

        {/* TOP LEFT */}

        <path
          d="M90 150 C180 170 230 220 330 310"
          stroke="url(#dataLine)"
          strokeWidth="1"
          fill="none"
        />

        <path
          d="M165 250 C230 260 280 290 350 325"
          stroke="url(#dataLine)"
          strokeWidth="1"
          fill="none"
        />

        <path
          d="M55 320 C180 315 260 320 350 335"
          stroke="url(#dataLine)"
          strokeWidth="1"
          fill="none"
        />

        {/* TOP RIGHT */}

        <path
          d="M910 150 C820 175 770 220 670 310"
          stroke="url(#dataLine)"
          strokeWidth="1"
          fill="none"
        />

        <path
          d="M835 250 C770 270 720 295 650 325"
          stroke="url(#dataLine)"
          strokeWidth="1"
          fill="none"
        />

        <path
          d="M950 325 C820 320 740 325 650 335"
          stroke="url(#dataLine)"
          strokeWidth="1"
          fill="none"
        />

        {/* BOTTOM LEFT */}

        <path
          d="M100 600 C210 570 270 525 350 470"
          stroke="url(#dataLine)"
          strokeWidth="1"
          fill="none"
        />

        <path
          d="M190 690 C260 620 300 560 370 480"
          stroke="url(#dataLine)"
          strokeWidth="1"
          fill="none"
        />

        {/* BOTTOM RIGHT */}

        <path
          d="M900 590 C820 555 760 520 675 475"
          stroke="url(#dataLine)"
          strokeWidth="1"
          fill="none"
        />

        <path
          d="M820 690 C760 620 710 560 650 485"
          stroke="url(#dataLine)"
          strokeWidth="1"
          fill="none"
        />

        {/* SMALL DATA NODES */}

        <g fill="#38bdf8" filter="url(#softGlow)">
          <circle cx="90" cy="150" r="2" />
          <circle cx="165" cy="250" r="2" />
          <circle cx="55" cy="320" r="2" />

          <circle cx="910" cy="150" r="2" />
          <circle cx="835" cy="250" r="2" />
          <circle cx="950" cy="325" r="2" />

          <circle cx="100" cy="600" r="2" />
          <circle cx="190" cy="690" r="2" />

          <circle cx="900" cy="590" r="2" />
          <circle cx="820" cy="690" r="2" />
        </g>
      </svg>

      {/* =====================================================
          CRM NODES
      ====================================================== */}

      {nodes.topLeft.map((node) => (
        <DataNode key={node.label} {...node} />
      ))}

      {nodes.topRight.map((node) => (
        <DataNode key={node.label} {...node} />
      ))}

      {nodes.bottomLeft.map((node) => (
        <DataNode key={node.label} {...node} />
      ))}

      {nodes.bottomRight.map((node) => (
        <DataNode key={node.label} {...node} />
      ))}

      {/* =====================================================
          DATABASE — BOTTOM RIGHT
      ====================================================== */}

      <div
        className="
          absolute
          bottom-[7%]
          right-[7%]
          hidden
          lg:block
        "
      >
        {/* Outer glow */}

        <div
          className="
            absolute
            -inset-
            rounded-full
            bg-cyan-300/15
            blur-[55px]
          "
        />

        {/* Database container */}

        <div
          className="
            relative
            flex
            h-32
            w-32
            items-center
            justify-center
            rounded-[32px]
            border
            border-white/90
            bg-white/65
            shadow-[0_25px_70px_rgba(14,165,233,0.14)]
            backdrop-blur-xl
            xl:h-40
            xl:w-40
            xl:rounded-[38px]
          "
        >
          {/* 3D extrusion */}

          <div
            className="
              absolute
              bottom-[-8px]
              left-1/2
              h-20
              w-20
              -translate-x-1/2
              rounded-[24px]
              bg-sky-400/10
              blur-[1px]
              xl:h-24
              xl:w-24
            "
          />

          {/* Inner database */}

          <div
            className="
              relative
              flex
              h-20
              w-20
              items-center
              justify-center
              rounded-[24px]
              border
              border-cyan-200
              bg-gradient-to-br
              from-white
              via-white
              to-cyan-50
              shadow-[inset_0_1px_0_rgba(255,255,255,0.95),0_12px_30px_rgba(14,165,233,0.12)]
              xl:h-24
              xl:w-24
            "
          >
            <Database
              className="h-10 w-10 text-sky-500 xl:h-12 xl:w-12"
              strokeWidth={1.6}
            />

            {/* Highlight */}

            <span
              className="
                absolute
                right-4
                top-3
                h-2
                w-2
                rounded-full
                bg-cyan-300
                shadow-[0_0_12px_rgba(34,211,238,0.8)]
              "
            />
          </div>
        </div>

        {/* Database label */}

        <div className="mt-3 text-center">
          <span className="text-[10px] font-medium tracking-[0.16em] text-slate-400 uppercase">
            Data Core
          </span>
        </div>
      </div>

      {/* =====================================================
          MOBILE ABSTRACT DATABASE
      ====================================================== */}

      <div
        className="
          absolute
          bottom-[4%]
          right-[6%]
          lg:hidden
        "
      >
        <div
          className="
            flex
            h-16
            w-16
            items-center
            justify-center
            rounded-[20px]
            border
            border-white/80
            bg-white/60
            shadow-[0_15px_40px_rgba(14,165,233,0.10)]
            backdrop-blur-xl
            opacity-70
          "
        >
          <Database
            className="h-7 w-7 text-sky-400"
            strokeWidth={1.7}
          />
        </div>
      </div>
    </div>
  );
}