import { useState } from 'react';
import { SidebarWrapper } from '@/components/sidebar-wrapper';
import { Button } from '@/components/ui/button';
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from '@/components/ui/dialog';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';

export default function Membership() {
    const [isDialogOpen, setIsDialogOpen] = useState(false)

    // Placeholder for payment processing integration.
    const handleProceed = () => {
        console.log('Proceed with credit card details')
    }

    const handleMembershipActionClick = () => {
        setIsDialogOpen(true)
    }

    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault()
        handleProceed()
        setIsDialogOpen(false)
    }

    return (
        <SidebarWrapper title="Membership">
            <div className="p-8 flex flex-col gap-4 login-card-enter">
                <h1 className="text-3xl font-bold mb-4">Change or Cancel Membership</h1>
                <p>Current Membership Status: </p>
                <Button className="w-3/5" variant="default" onClick={handleMembershipActionClick}>Change to Standard</Button>
                <Button className="w-3/5" variant="default" onClick={handleMembershipActionClick}>Change to Pro</Button>
                <Button className="w-3/5" variant="default" onClick={handleMembershipActionClick}>Change to Pro+</Button>
                <Button className="w-3/5" variant="default" onClick={handleMembershipActionClick}>Cancel Membership</Button>
            </div>

            <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
                <DialogContent>
                    <DialogHeader>
                        <DialogTitle>Credit Card Information</DialogTitle>
                        <DialogDescription>
                            Enter your payment details to continue.
                        </DialogDescription>
                    </DialogHeader>

                    <form className="space-y-4" onSubmit={handleSubmit}>
                        <div className="space-y-2">
                            <Label htmlFor="card-full-name">Full Name</Label>
                            <Input id="card-full-name" placeholder="Alex Johnson" required />
                        </div>

                        <div className="space-y-2">
                            <Label htmlFor="card-number">Number</Label>
                            <Input
                                id="card-number"
                                inputMode="numeric"
                                autoComplete="cc-number"
                                placeholder="1234 5678 9012 3456"
                                required
                            />
                        </div>

                        <div className="grid grid-cols-2 gap-4">
                            <div className="space-y-2">
                                <Label htmlFor="card-expiry">Date of Expiry</Label>
                                <Input
                                    id="card-expiry"
                                    autoComplete="cc-exp"
                                    placeholder="MM/YY"
                                    required
                                />
                            </div>
                            <div className="space-y-2">
                                <Label htmlFor="card-cvc">CVC</Label>
                                <Input
                                    id="card-cvc"
                                    inputMode="numeric"
                                    autoComplete="cc-csc"
                                    placeholder="123"
                                    required
                                />
                            </div>
                        </div>

                        <DialogFooter>
                            <Button type="button" variant="outline" onClick={() => setIsDialogOpen(false)}>
                                Cancel
                            </Button>
                            <Button type="submit">Proceed</Button>
                        </DialogFooter>
                    </form>
                </DialogContent>
            </Dialog>
        </SidebarWrapper>
    );
}