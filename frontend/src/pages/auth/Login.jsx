import { useState } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import { useForm } from "react-hook-form";
import { toast } from "sonner";
import { Mail, Lock } from "lucide-react";
import { AuthShell } from "./AuthShell";
import { Button, Field, Input } from "../../components/ui";
import { useAuth } from "../../context/AuthContext";

export default function Login() {
  const { login } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const [submitting, setSubmitting] = useState(false);

  const {
    register,
    handleSubmit,
    setValue,
    formState: { errors },
  } = useForm({ defaultValues: { email: "", password: "" } });

  const onSubmit = async (data) => {
    setSubmitting(true);
    try {
      const user = await login(data);
      toast.success(`Welcome back, ${user.name.split(" ")[0]} 👋`);
      navigate(location.state?.from?.pathname || "/", { replace: true });
    } catch (err) {
      toast.error(err.message || "Login failed");
    } finally {
      setSubmitting(false);
    }
  };

  // Convenience: pre-fill the seeded demo credentials.
  const useDemo = () => {
    setValue("email", "admin@test.com");
    setValue("password", "Anonymous0!");
  };

  return (
    <AuthShell>
      <h1 className="font-display text-2xl font-bold tracking-tight text-slate-900 sm:text-[26px]">Welcome back</h1>
      <p className="mt-2 text-sm leading-6 text-slate-500">
        Sign in to [YOUR CRM] workspace.
      </p>

      <form onSubmit={handleSubmit(onSubmit)} className="mt-8 space-y-4">
        <Field label="Email" error={errors.email?.message}>
          <div className="relative">
            <Mail className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-ink-soft" />
            <Input
              type="email"
              placeholder="you@company.com"
              className="pl-9"
              {...register("email", { required: "Email is required" })}
            />
          </div>
        </Field>

        <Field label="Password" error={errors.password?.message}>
          <div className="relative">
            <Lock className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-ink-soft" />
            <Input
              type="password"
              placeholder="••••••••"
              className="pl-9"
              {...register("password", { required: "Password is required" })}
            />
          </div>
        </Field>

        <Button type="submit" className="w-full" size="lg" loading={submitting}>
          Sign in
        </Button>
      </form>

      <button
        type="button"
        onClick={useDemo}
        className="
          mt-3
          w-full
          rounded-full
          border
          border-dashed
          border-cyan-300/80
          bg-white/40
          py-2.5
          text-sm
          font-medium
          text-sky-700
          transition-all
          duration-200
          hover:border-cyan-400
          hover:bg-cyan-50/70
          hover:shadow-[0_8px_24px_rgba(14,165,233,0.08)]
        "
      >
        Try the demo account
      </button>

      <p className="mt-6 text-center text-sm text-ink-soft">
        Don't have an account?{" "}
        <a href="https://portfolio-app-blue-rho.vercel.app/" className="font-semibold text-brand-700 hover:underline">
          Create one
        </a>
      </p>
    </AuthShell>
  );
}
